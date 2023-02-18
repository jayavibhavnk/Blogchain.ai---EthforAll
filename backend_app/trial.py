import json
import requests
#trial for ethforall


URL = "http://127.0.0.1:8000/blog"

#URL = "https://axgcmh.deta.dev/blog"

body="""Ferrari is an Italian luxury sports car manufacturer based in Maranello, Italy. Founded by Enzo Ferrari in 1947, Ferrari has become one of the world's most well-known and recognizable car brands. The company is known for producing high-performance cars that offer speed, power, and sophistication.

Ferrari's signature product is the Ferrari sports car, which is known for its sleek design, powerful engine, and exceptional handling. Over the years, the company has introduced several iconic models, including the Ferrari 250 GTO, the Ferrari 288 GTO, the Ferrari F40, the Ferrari Enzo, and the Ferrari LaFerrari. Each of these models has become a classic in its own right and has helped cement Ferrari's reputation as a leading producer of premium sports cars.

In addition to its sports cars, Ferrari has also produced several racing cars over the years. The company has a long and successful history in motorsport, and it has won numerous races and championships in a variety of motorsport categories, including Formula One, endurance racing, and sports car racing.

Ferrari is also known for its innovative use of technology. The company has been at the forefront of automotive engineering, and it has consistently pushed the boundaries of what is possible with modern sports cars. For example, Ferrari was one of the first car manufacturers to incorporate electronic driver aids, such as traction control and stability control, into its cars.

Despite its rich heritage and reputation for producing some of the world's finest sports cars, Ferrari is not content to rest on its laurels. The company continues to innovate and push the boundaries of what is possible, and it is constantly working to improve its products and create new and exciting vehicles for its customers.

In conclusion, Ferrari is a true icon of the automotive world. With its rich heritage, high-performance cars, and commitment to innovation, Ferrari is a brand that is synonymous with excellence and sophistication. Whether you're a fan of sports cars or just admire Ferrari's engineering and design, there is no denying that this company is one of the most important and influential in the automotive industry."""

PARAMS = {"title": "Ferrari",
  "blog_content":body}

r = requests.post(url = URL, json=PARAMS)
#print(type(r))
print(r.json())