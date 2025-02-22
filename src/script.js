import { Storage } from "@capacitor/storage";
import { App } from "@capacitor/app";

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

        if (window.location.href !== "https://localhost/") {
            window.location.href = prevPage;
        } else {
            App.exitApp();
        }
    });
} else {
  alert('bai')
}
  }

export { handleBackButton };