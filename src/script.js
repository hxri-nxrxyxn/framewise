import { Storage } from "@capacitor/storage";
import { App } from "@capacitor/app";
import { TextToSpeech } from "@capacitor-community/text-to-speech";
const baseUrl = "https://api2.laddu.cc/api/v1";
const socketUrl = "wss://api.laddu.cc/ws";
import { goto } from "$app/navigation";
let videoElement = null;
let canvasElement = null;
let ctx = null;
let socket = null;

async function setToken(token) {
  await Storage.set({
    key: "token",
    value: token,
  });
}

function handleBackButton(fallbackUrl) {
  if (typeof window !== "undefined" && typeof sessionStorage !== "undefined") {
    sessionStorage.setItem("fallbackPage", fallbackUrl);

    App.addListener("backButton", () => {
      const prevPage = sessionStorage.getItem("fallbackPage");

      if (
        window.location.href !== "https://localhost/" &&
        window.location.href !== "https://localhost/home"
      ) {
        goto(prevPage, { replaceState: true });
      } else {
        App.exitApp();
      }
    });
  } else {
  }
}

async function checkUser() {
  const { value } = await Storage.get({ key: "token" });
  console.log(value);
  if (!value) {
    goto("login", { replaceState: true });
    return;
  }
  const response = await fetch(`${baseUrl}/verify`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${value}`,
    },
  });
  const res = await response.json();
  if (!response.ok) {
    alert(res.message);
    await logout();
    goto("/login", { replaceState: true });
    return;
  }
  const id = res.id;
  const response2 = await fetch(`${baseUrl}/users/${id}`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  });
  const res2 = await response2.json();
  if (!response2.ok) {
    alert(res2.message);
    return;
  }
  return res2.data;
}

async function logout() {
  try {
    await Storage.remove({ key: "token" });
    goto("/login", { replaceState: true });
  } catch (error) {
    console.error("Error:", error);
  }
}

async function login(data) {
  try {
    console.log(data);
    const response = await fetch(`${baseUrl}/login`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });
    const res = await response.json();
    if (!response.ok) {
      alert(res.message);
      return;
    }
    await setToken(res.token);
    goto("/home", { replaceState: true });
  } catch (error) {
    console.log(error);
  }
}

async function signup(data) {
  try {
    console.log(data);
    const response = await fetch(`${baseUrl}/register`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });
    const res = await response.json();
    if (!response.ok) {
      alert(res.message);
      return;
    }
    await setToken(res.token);
    goto("/", { replaceState: true });
  } catch (error) {
    console.log(error);
  }
}

function startWebsocket() {
  try {
    socket = new WebSocket(socketUrl);
    socket.onopen = function (e) {
      console.log("[open] Connection established");
      let my_string, result;

      socket.onmessage = (event) => {
        my_string = event.data;
        result = my_string.split(",");
        document.getElementById("message").textContent = result[1];
        speakText(result[1]);
      };

      socket.onclose = function (event) {
        if (event.wasClean) {
          console.log(
            `[close] Connection closed cleanly, code=${event.code} reason=${event.reason}`,
          );
        } else {
          console.log("[close] Connection died");
        }
      };

      socket.onerror = function (error) {
        console.log(`[error] ${error.message}`);
      };
    };
  } catch (error) {
    alert("Error accessing WebSocket " + error);
  }
}

async function startCamera() {
  videoElement = document.createElement("video");
  videoElement.autoplay = true;
  videoElement.playsInline = true; // Ensure iOS compatibility
  videoElement.style.width = "100%"; // Adjust size as needed
  videoElement.style.height = "100%"; // Adjust size as needed

  document.getElementById("pimage").appendChild(videoElement); // Add to page

  try {
    const stream = await navigator.mediaDevices.getUserMedia({ video: true });
    videoElement.srcObject = stream;

    canvasElement = document.createElement("canvas");
    ctx = canvasElement.getContext("2d");
  } catch (error) {
    console.error("Error accessing camera:", error);
  }
}

async function captureFrame() {
  if (!videoElement || !canvasElement || !ctx) {
    return null;
  }

  canvasElement.width = videoElement.videoWidth;
  canvasElement.height = videoElement.videoHeight;

  ctx.drawImage(videoElement, 0, 0, canvasElement.width, canvasElement.height);

  // Convert to Base64
  return canvasElement.toDataURL("image/jpeg", 0.5); // or "image/png"
}

function sendToBackend(base64String) {
  if (socket.readyState === WebSocket.OPEN) {
    socket.send(base64String);
  }
}

function stopCamera() {
  if (stream) {
    stream.getTracks().forEach((track) => track.stop()); // Stop all amera tracks
  }

  if (videoElement) {
    videoElement.remove(); // Remove the video from the page
    videoElement = null; // Reset variable
    stream = null; // Reset stream
  }
}

function cameraBack() {
  if (typeof window !== "undefined" && typeof sessionStorage !== "undefined") {
    App.addListener("backButton", () => {
      const prevPage = sessionStorage.getItem("fallbackPage");
      stopCamera();
    });
  } else {
  }
}

async function speakText(text) {
  try {
    await TextToSpeech.speak({
      text: text,
      lang: "en-US", // Change language if needed
      rate: 1.0, // Speech speed (0.5 - 2.0)
      pitch: 1.0, // Pitch (0.5 - 2.0)
      volume: 1.0, // Volume (0.0 - 1.0)
      category: "ambient",
    });
  } catch (error) {
    console.error("TTS Error:", error);
  }
}

export {
  handleBackButton,
  checkUser,
  logout,
  login,
  signup,
  startWebsocket,
  startCamera,
  captureFrame,
  sendToBackend,
  cameraBack,
  stopCamera,
  speakText,
};
