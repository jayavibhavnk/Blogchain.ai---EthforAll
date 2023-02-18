import yake
import requests
from moralis import evm_api
import json
import base64
from pysteg_new.usage_example import image_encryptor,image_decryptor
import nft_storage
from nft_storage.api import nft_storage_api
import subprocess
import time

image0=""

def blog_data_gen(blog_json):
    new_json=blog_json
    blog_content=blog_json['blog_content']
    #keywords
    kw_extractor = yake.KeywordExtractor()
    keywords = kw_extractor.extract_keywords(blog_content)
    k_1=keywords[:5]
    lemmas=[i[0] for i in k_1]
    try:
        l=[]
        for i in lemmas:
            response = requests.get('https://lexica.art/api/v1/search?q={}'.format(i))
            lex_req=response.json()
            img=list(lex_req.values())[0][0]['src']
            l.append(img)
    except:
        print("loading generic images")
        l=['https://lexica-serve-encoded-images2.sharif.workers.dev/md/4da8f335-5664-441c-a828-9c3ee8b17ea8',
          'https://lexica-serve-encoded-images2.sharif.workers.dev/md/0088f0a6-eeca-4423-a358-f3aa427ead50',
          'https://lexica-serve-encoded-images2.sharif.workers.dev/md/0854a95e-c477-4b69-8395-5022b8180a09',
          'https://lexica-serve-encoded-images2.sharif.workers.dev/md/252c8302-c62b-4a86-84f1-5a9cc153666c',
          'https://lexica-serve-encoded-images2.sharif.workers.dev/md/48e2abb5-f787-455e-a995-07aa968c072e']
    #print(l)
    for i in range(5):
        new_json['image{}'.format(i)]=l[i]
    new_json["keywords"]=lemmas
    return new_json

def json_t_base64(data):
    json_string = json.dumps(data)
    base64_bytes = base64.b64encode(json_string.encode("utf-8"))
    return(base64_bytes.decode("utf-8"))

def ipfsupload(BASE_64,title):
    api_key="xtix2Z0SyxNsbqZ20uW9pN11Thou0EmaDwmSphrP6ah9JNsHo0ZedLgWzTVtvRbL"
    body=[
    {
        "path":"report{}".format(title),
        "content":BASE_64,
    }
    ]
    result=evm_api.ipfs.upload_folder(
    api_key=api_key,
    body=body,
    )
    return result[0]["path"]

def json_to_image(json_file):
    url=json_file['image0']
    try:
        response = requests.get(url)
    except:
        print("could not load image")

    if response.status_code == 200:
        with open("pre_nft.jpg", "wb") as f:
            f.write(response.content)
        print("Image saved successfully.")
    else:
        print("Failed to retrieve image from URL.")

def image_to_base64(img_path):
    with open(img_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
    return(encoded_string)

def nftupload(BASE_64,title):
    api_key="xtix2Z0SyxNsbqZ20uW9pN11Thou0EmaDwmSphrP6ah9JNsHo0ZedLgWzTVtvRbL"
    body=[
    {
        "path":"nftof{}".format(title),
        "content":BASE_64,
    }
    ]
    result=evm_api.ipfs.upload_folder(
    api_key=api_key,
    body=body,
    )
    return result[0]["path"]


import nft_storage
from nft_storage.api import nft_storage_api

def nft_creator(json_file):
    try:
        json_to_image(json_file)
    except:
        print("could not create image")
        return "nft link"
    in_path = "pre_nft.jpg"
    out_path = "new_imge.png"
    password = "12345678"
    message = json_file['blog_content']
    try:
        image_encryptor(in_path,out_path,password,message)
    except:
        print("nft could not be created")


    # base_file = image_to_base64("new_imge.png")
    # title = json_file['title']
    #ipfs/fvm
    try:
        configuration = nft_storage.Configuration(
                access_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkaWQ6ZXRocjoweDJGZjJmQjcwY2YzODk2QkZkRTg0NDJEOGQ3NmIwREY0N0QzYTE0OTciLCJpc3MiOiJuZnQtc3RvcmFnZSIsImlhdCI6MTY3NjE4NTkyOTY5MywibmFtZSI6ImV0aGZvcmFsbCJ9.rudsWWUVpG9zX7TGOSAbsGoLoBFuzwzyyM4J3fjbokE')
                
        api_client = nft_storage.ApiClient(configuration)
        api_instance = nft_storage_api.NFTStorageAPI(api_client)    
        body = open(r'C:\Users\jayav\Desktop\ethforall\backend_app\new_imge.png','rb')
        api_response = api_instance.store(body, _check_return_type=False)
        print("nft successfully uploaded")
    except:
        print("could not upload nft")
    return "https://ipfs.io/ipfs/"+api_response['value']['cid']
    #return nftupload(base_file,title)

def upload_to_mongo(mongo_json):
    try:
        url = "https://data.mongodb-api.com/app/data-stoly/endpoint/data/v1/action/insertOne"

        headers = {
            "Content-Type": "application/json",
            "apiKey": "V2jAj0WKRWitf1Tzw0UdTg5cCcWckSZLErF4AAOcVEJavrOO65MY6Ia65uOQDazQ"
        }

        payload = {
            "dataSource": "Cluster0",
            "database": "Ethforall_blogs",
            "collection": "blogs",
            "document":mongo_json
        }
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        print(response.text)
    except:
        print("could not upload to mongo")

def push():
    node_script_path = r'C:\Users\jayav\Desktop\ethforall\backend_app\scripts2.js'
    result = subprocess.run(['node', node_script_path], capture_output=True, text=True)

def blog_to_ipfs(blog_json):
    new_json = blog_data_gen(blog_json)
    title = new_json["title"]
    author = new_json['author']
    category = new_json['category']
    BASE_64_json = json_t_base64(new_json)
    try:
        ipfs_link = ipfsupload(BASE_64_json,title)
        print("successfully uploaded to ipfs")
    except:
        print("could not uplaod to ipfs")
    
    nft = nft_creator(new_json)
    #dummy nft
    #nft="ipfs/fvm link after image steganography"
    #uploading to mongo
    mongo_json = new_json
    mongo_json['ipfs'] = ipfs_link
    mongo_json['nft'] = nft
    
    upload_to_mongo(mongo_json)

    print("done")

    #push
    try:
        
        file = open('scripts2.js','w')
        x = """
        import * as PushAPI from "@pushprotocol/restapi";
        import * as ethers from "ethers";

        const Pkey = `0xbfda15ce3b8a6405882e7571d9953e9435d45d713eff2fee080b9a4873094d05`;
        const signer = new ethers.Wallet(Pkey);
        const sendNotification = async () => {
            try {
                const apiResponse = await PushAPI.payloads.sendNotification({
                    signer,
                    type: 4, // subset
                    identityType: 2, // direct payload
                    notification: {
                        title: `Web3 Notifications`,
                        body: `Hello`,
                    },
                    payload: {
                        title: `Here's a new blog!`,
                        body: `%s`,
                        cta: "",
                        img: "%s",
                    },
                    recipients: [
                        "eip155:5:0x25cEA86d3309AFA37bEd0412810c5a4d9Ffdb9D7",
                        "eip155:5:0xAdF8af32653ffdF5c5cD4ae760b54598a51536d3",
                        "eip155:5:0xDfB90E5f7f3f62aC4B15b431F4674354A21eed56",
                    ], // recipients addresses
                    channel: "eip155:5:0xE49ab5380e332AC3456bB33cf588Db2770536f27", // your channel address
                    env: "staging",
                });

                // apiResponse?.status === 204, if sent successfully!
                console.log("API repsonse: ", apiResponse);
            } catch (err) {
                console.error("Error: ", err);
            }
        };

        sendNotification();""" %("here's a blog on {} \n by {} \n category - {}".format(title,author,category),str(nft))
        #print(x)
        file.write(x)
        file.close()
        time.sleep(5)
        push()
        print("successfully sent message")
    except:
        print("could not send push")

    return True



##trial
# blog = """Lamborghini is an Italian luxury sports car manufacturer that was founded in 1963 by Ferruccio Lamborghini. The company is known for producing some of the most stylish, high-performance vehicles in the world, and its cars are prized for their distinctive designs, powerful engines, and impressive speed.

# The first Lamborghini car was the 350 GT, which was released in 1964. This car was followed by a series of iconic models, including the Miura, Countach, Diablo, and Murcielago. Today, the company offers a range of sports cars, including the Aventador, Huracan, and Urus.

# One of the defining characteristics of Lamborghini cars is their powerful engines. Many of the company's vehicles are equipped with V12 engines, which are capable of producing incredibly high amounts of power and torque. This gives the cars an incredible level of acceleration and speed, making them some of the fastest and most thrilling vehicles on the road.

# Another defining feature of Lamborghini cars is their unique and eye-catching designs. The company's vehicles are known for their bold, aggressive styling, and they often feature sharp lines, angular shapes, and angular body panels. This design aesthetic is part of what makes Lamborghini cars so recognizable and iconic.

# In recent years, Lamborghini has also been at the forefront of electric vehicle technology. In 2019, the company introduced the Lamborghini Terzo Millennio, an all-electric concept car that showcased the company's vision for the future of sports cars.

# Overall, Lamborghini is a company that is synonymous with luxury, performance, and style. Whether you are a car enthusiast, a collector, or simply someone who appreciates beautiful vehicles, there is no denying the appeal of a Lamborghini. These cars are some of the most sought-after and admired vehicles in the world, and they continue to push the boundaries of what is possible in the world of high-performance sports cars"""
# blog_json = {
#     "title":"Lamborghini car",
#     "blog_content":blog
# }

# print(blog_to_ipfs(blog_json))
    
