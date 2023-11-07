import time
import requests
import logging
import argparse


class LLMFlaskClient:
    def __init__(self, ip: str, port: int, max_retry: int = 3):
        self.ip = ip
        self.port = port

        self.url_prefix_format = 'http://{}:{}/'
        self.url = self.url_prefix_format.format(self.ip, self.port)
        self.max_retry = max_retry

        self.logger = logging.getLogger()
        self.logger.addHandler(logging.StreamHandler())
        self.logger.handlers[0].setFormatter(logging.Formatter("%(message)s"))

    def _request(self, name: str, data: dict):
        for _ in range(self.max_retry):
            try:
                self.logger.info(f'{name}\ndata: {data}')
                response = requests.post(self.url + name, json=data).json()
            except Exception as e:
                self.logger.warning('error: ', repr(e))
                time.sleep(1)
                continue
            if response['code'] == 0:
                return response['output']
            else:
                raise Exception(response['error_msg'])
        raise Exception("Web service failed. Please retry or contact with manager")

    def run(self, message: str) -> str:
        try:
            return self._request('ask_llm_for_answer', {'user_text': message})
        except Exception as e:
            return f"Error: {repr(e)}"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--ip', required=True)
    parser.add_argument('-p', '--port', required=True)
    parser.add_argument('--debug', action='store_true')
    args = parser.parse_args()
    if args.debug:
        logging.getLogger().setLevel(logging.INFO)
    else:
        logging.getLogger().setLevel(logging.WARNING)

    client = LLMFlaskClient(args.ip, args.port)
    print(client.run('Please concatenate string "1+" and "1=3". Only give me the result without "".'))
