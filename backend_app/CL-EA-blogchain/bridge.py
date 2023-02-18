import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


class Bridge(object):

    def __init__(
        self,
        retries=3,
        backoff_factor=0.3,
        status_forcelist=(500, 502, 504),
    ):
        self.session = requests.Session()
        retry = Retry(
            total=retries,
            read=retries,
            connect=retries,
            backoff_factor=backoff_factor,
            status_forcelist=status_forcelist,
        )
        adapter = HTTPAdapter(max_retries=retry)
        self.session.mount('http://', adapter)
        self.session.mount('https://', adapter)

    def request(self, url, json, headers={}, timeout=15):
        try:
            return self.session.post(url,
                                    json=json,
                                    headers=headers,
                                    timeout=timeout)
        except Exception as e:
            raise e

    def close(self):
        self.session.close()

#br = Bridge()
# #p={ 
#                     "blog_content":"lamborghini mclaren ferrari mercedes benz",
#                 "title":"carss"
# }
#response = br.request("https://axgcmh.deta.dev/blog",json=p)

# body="""Lamborghini is an Italian luxury sports car manufacturer that was founded in 1963 by Ferruccio Lamborghini. The company is known for producing some of the most stylish, high-performance vehicles in the world, and its cars are prized for their distinctive designs, powerful engines, and impressive speed.

# The first Lamborghini car was the 350 GT, which was released in 1964. This car was followed by a series of iconic models, including the Miura, Countach, Diablo, and Murcielago. Today, the company offers a range of sports cars, including the Aventador, Huracan, and Urus.

# One of the defining characteristics of Lamborghini cars is their powerful engines. Many of the company's vehicles are equipped with V12 engines, which are capable of producing incredibly high amounts of power and torque. This gives the cars an incredible level of acceleration and speed, making them some of the fastest and most thrilling vehicles on the road.

# Another defining feature of Lamborghini cars is their unique and eye-catching designs. The company's vehicles are known for their bold, aggressive styling, and they often feature sharp lines, angular shapes, and angular body panels. This design aesthetic is part of what makes Lamborghini cars so recognizable and iconic.

# In recent years, Lamborghini has also been at the forefront of electric vehicle technology. In 2019, the company introduced the Lamborghini Terzo Millennio, an all-electric concept car that showcased the company's vision for the future of sports cars.

# Overall, Lamborghini is a company that is synonymous with luxury, performance, and style. Whether you are a car enthusiast, a collector, or simply someone who appreciates beautiful vehicles, there is no denying the appeal of a Lamborghini. These cars are some of the most sought-after and admired vehicles in the world, and they continue to push the boundaries of what is possible in the world of high-performance sports cars."""

# PARAMS = {"title": "Premier League",
#   "blog_content":body}

# r = requests.post(url="https://axgcmh.deta.dev/blog",json=PARAMS)

#print(response.text)