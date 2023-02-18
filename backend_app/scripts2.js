
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
                        body: `here's a blog on fireworld 
 by ntn 
 category - Social`,
                        cta: "",
                        img: "https://ipfs.io/ipfs/bafybeigw7fzh62mhd5wvjjlkmnsswmmxlrr4ehyz62ftrmg6jzvhmjdj6y",
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