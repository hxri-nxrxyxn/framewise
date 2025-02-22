import { Storage } from "@capacitor/storage";
import { App } from "@capacitor/app";
const baseUrl = "https://api.laddu.cc/api/v1";
const socketUrl = "wss://api.laddu.cc/api/v1";
import { goto } from '$app/navigation';


async function setToken(token) {
    await Storage.set({
      key: "token",
      value: token,
    });
  }

function handleBackButton(fallbackUrl) {
  if (typeof window !== 'undefined' && typeof sessionStorage !== 'undefined') {
    sessionStorage.setItem("fallbackPage", fallbackUrl);

    App.addListener("backButton", () => {
        const prevPage = sessionStorage.getItem("fallbackPage");

        if (window.location.href !== "https://localhost/login") {
            goto(prevPage, { replaceState: true });
        } else {
            App.exitApp();
        }
    });
} else {
}
  }

async function checkUser() {
  const { value }  = await Storage.get({ key: "token" });
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
    goto("/login", { replaceState: true })
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
    goto("/login", { replaceState: true })
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
    goto("/", { replaceState: true })
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
    goto("/", { replaceState: true })
  } catch (error) {
    console.log(error);
  }
}

function startWebsocket() {
  try{
    let socket = new WebSocket(socketUrl);
    socket.onopen = function (e) {
      alert("[open] Connection established");
  
      socket.onclose = function (event) {
        if (event.wasClean) {
          alert(`[close] Connection closed cleanly, code=${event.code} reason=${event.reason}`);
        } else {
          alert("[close] Connection died");
        }
      };
  
      socket.onerror = function (error) {
        alert(`[error] ${error.message}`);
      };
    }
  }
  catch(error){
    alert("Error accessing WebSocket " + error);
  }
}

export { handleBackButton , checkUser, logout, login, signup };