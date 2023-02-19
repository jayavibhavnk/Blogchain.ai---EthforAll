import { createSocketConnection, EVENTS } from "@pushprotocol/socket";
const pushSDKSocket = createSocketConnection({
  user: "eip155:0x25cEA86d3309AFA37bEd0412810c5a4d9Ffdb9D7",
  env: "staging",
  apiKey:
    "6XC8wHsTi1.vLdCazQwnv5qdjNbXAFpwPVyJOWY47GLIekPqJsQuYOCfFUVmSxolhmEUywxF51P",
  socketType: "chat",
  socketOptions: { autoConnect: true, reconnectionAttempts: 3 },
});
pushSDKSocket.on(EVENTS.CONNECT, () => {});

pushSDKSocket.on(EVENTS.DISCONNECT, () => {});

pushSDKSocket.on(EVENTS.CHAT_RECEIVED_MESSAGE, (message) => {
  // message is the message object data whenever a new message is received
});
