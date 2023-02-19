import * as PushAPI from "@pushprotocol/restapi";
import * as ethers from "ethers";

//const PK = ""; // channel private key

const Pkey = `0xbfda15ce3b8a6405882e7571d9953e9435d45d713eff2fee080b9a4873094d05`;
const signer = new ethers.Wallet(Pkey);
const sendNotification = async () => {
  try {
    const apiResponse = await PushAPI.payloads.sendNotification({
      signer,
      type: 4, // subset
      identityType: 2, // direct payload
      notification: {
        title: `Blogchain.ai`,
        body: `New blog available!`,
      },
      payload: {
        title: `Hey there! A new blog is available`,
        body: `Here's a new blog on Atlantis \n by Jayavibhav NK \n category - Nature`,
        cta: "",
        img: "https://ipfs.io/ipfs/bafybeieeqqdx7tlonviig2zqq2leikk4yrq27zpk2ajekkqup2usaksjku",
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
sendNotification();
