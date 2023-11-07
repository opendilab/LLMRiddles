from transformers import AutoModelForCausalLM, AutoTokenizer
from flask import Flask, request
import argparse
import logging


class LLMInstance:

    def __init__(self, model_path: str, device: str = "cuda"):

        self.model = AutoModelForCausalLM.from_pretrained(model_path)
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.model.to(device)
        self.device = device

    def query(self, message):
        try:
            messages = [
                {"role": "user", "content": message},
            ]
            encodeds = self.tokenizer.apply_chat_template(messages, return_tensors="pt")
            model_inputs = encodeds.to(self.device)

            generated_ids = self.model.generate(model_inputs, max_new_tokens=1000, do_sample=True)
            decoded = self.tokenizer.batch_decode(generated_ids)

            # output is the string decoded[0] after "[/INST]". There may exist "</s>", delete it.
            output = decoded[0].split("[/INST]")[1].split("</s>")[0]
            return {
                'code': 0,
                'ret': True,
                'error_msg': None,
                'output': output
            }
        except Exception as e:
            return {
                'code': 1,
                'ret': False,
                'error_msg': str(e),
                'output': None
            }


def create_app(core):
    app = Flask(__name__)

    @app.route('/ask_llm_for_answer', methods=['POST'])
    def ask_llm_for_answer():
        user_text = request.json['user_text']
        return core.query(user_text)

    return app


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--model_path', required=True, default='Mistral-7B-Instruct-v0.1', help='the model path of reward model')
    parser.add_argument('--ip', default='0.0.0.0')
    parser.add_argument('-p', '--port', default=8001)
    parser.add_argument('--debug', action='store_true')
    args = parser.parse_args()

    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)
    else:
        logging.getLogger().setLevel(logging.INFO)
    logging.getLogger().addHandler(logging.StreamHandler())
    logging.getLogger().handlers[0].setFormatter(logging.Formatter("%(message)s"))

    core = LLMInstance(args.model_path)
    app = create_app(core)
    app.run(host=args.ip, port=args.port)
