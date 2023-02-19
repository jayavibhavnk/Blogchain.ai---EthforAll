# BlogChain.ai - EthforAll

Blogs are a forum for individuals and organisations to communicate their thoughts, ideas, and experiences with an audience from all over the world. They have become an irreplaceable medium of sharing information in the modern era, but due to reduced attention spans, many find it difficult to sit through walls of text without any illustrations, leading to limited reach and comprehensibilty of the content. According to research, image-based blogs have higher user engagement and readership than text-based blogs as they appeal to visual learners better.

Through _BlogChain.ai_, we hope to help both bloggers and readers have a better experience in posting and consuming content on the internet. Want to increase traffic on your blogs or get the entire gist of the content in a few seconds? Don't worry, we've got your back.

*BlogChain.ai* is a web3 based blogging platform which integrates the powerful generative capabilities of AI into blockchain. Our AI specially generates images which are used as NFTs and are oriented towards the written material of the blog. This enables bloggers to make their writing visually appealing, while also making a unique NFT based on the highlighted content in the blog. Our site creates an NFT using the cover image of the blog and encodes the blog text into the image using image steganography. This helps users share their content using a single NFT, thus increasing the shareability and readability of these blogs.

This has been developed using web 3.0 technologies that enable decentralization, personalization, immersiveness, and a token-driven economy. It provides user with a personalized web surfing experience. The project aims at making blog sharing decentralised using web 3.0 technologies like **FVM**, **Arcana**, **IPFS**, **PUSH Protocol**, **Chainlink** etc.


## Technologies used for development - 

- ### Arcana : 

BlogChain.ai values user privacy and makes sure that the blog content isn't plagiarised and reused. This is doubly ensured by the blockchain being used and the unique NFTs that are generated, based on the content of the blog. Since user authentication is one of the most important features for our website, the usage and creation of blogs on our platform requires a valid user, and this is confirmed by the authentication mechanism powered by Arcana.

We integrated ARCANA SDK for user authentication in our website. It enables a familiar web2 user onboarding experience in our web3 application. The user is required to login to access the features of the website, such as to read and create blogs. The user can create visually appealling blog images by creating NFTs with the blog content only after verification. Users can either use their google account or email id to login and use the features of the platform.

The implementation of Arcana SDK in our project is shown in the following demo:

https://www.youtube.com/watch?v=XMHn-AmlLaI


- ### PUSH Protocol : 

After successful authentication, the user can create a blog which is processed on the backend to generate an AI image and this, in turn, is used to create an NFT. This NFT is minted with the smart contract deployed to FVM. Once the NFT is minted, it generates a PUSH notification that is sent to all the users across the channel. The PUSH notification shows the members the details of the blog as well as the NFT image.

Here, is a demonstration of PUSH notifications implemented in the project to send notifications to all users about the newly minted NFTs and the created blogs:-

https://youtu.be/OSp0tJwj0WU

- ### Chainlink : 

Our project focuses on creating NFTs from AI generated images using specific keywords for a blog. This process can prove to be expensive on the blockchain, and hence we implemented Chainlink for it to be handled off-chain. We used Chainlink to access a custom created external api, which was hosted online to perform the computations and load the data onto the blockchain.
A Chainlink bridge was implemented and hosted locally using a docker container.

Here, is the demonstration of Chainlink into the project to provide data and information from off-blockchain sources to on-blockchain smart contracts:-

https://youtu.be/y3vJxndO7gA

- ### FVM and IPFS : 

Our project creates AI generated images for blogs which are then converted to NFTs. This NFT is encoded with the blog text and uploaded onto nft.storage, using the api to get the CID. Once the NFT is uploaded, it is minted using smart contracts, which are deployed on File Coin Virtual Machine (FVM) to generate the accessible link. This link is the NFT which is stored in IPFS and is used to display the NFT on push notifications, as well as on the website. 

The smart contract is deployed on FVM, and is based on ERC721 contract. This provides a standard for representing ownership of non - fungible tokens (NFTs), with guidelines and methods for minting NFTs.
