from bridge import Bridge


class Adapter:

    def __init__(self,data):
        #self.id = input.get('id', '1')
        #self.request_data = input.get('data')
        self.data = data
        self.bridge = Bridge()
        self.create_request()

    def validate_request_data(self):
        if self.request_data is None:
            return False
        if self.request_data == {}:
            return False
        return True

    def set_params(self):
        self.staion_id = self.request_data.get("station_id")

    def create_request(self):
        try:
            base_url="https://axgcmh.deta.dev/blog"
            params = {
                "blog_content":"lamborghini mclaren ferrari mercedes benz",
                "title":"carss"
            }
            response = self.bridge.request(url = base_url, json = self.data)
            r = response.json()
            return r
        except:
            print("error")
        finally:
            self.bridge.close()

    def result_success(self, data):
        self.result = {
            'jobRunID': self.id,
            'data': data,
            'result': self.result,
            'statusCode': 200,
        }

    def result_error(self, error):
        self.result = {
            'jobRunID': self.id,
            'status': 'errored',
            'error': f'There was an error: {error}',
            'statusCode': 500,
        }
