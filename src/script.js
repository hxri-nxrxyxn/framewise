import { Storage } from "@capacitor/storage";

async function setToken(token) {
    await Storage.set({
      key: "token",
      value: token,
    });
  }