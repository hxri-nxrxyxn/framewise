<script>
  import {
    startWebsocket,
    startCamera,
    sendToBackend,
    cameraBack,
    captureFrame,
  } from "../../script";
  import { onMount } from "svelte";
  cameraBack();

  onMount(() => {
    startWebsocket();
    startCamera();
  });

  setInterval(async () => {
    const base64Frame = await captureFrame();
    if (base64Frame) {
      sendToBackend(base64Frame);
    }
  }, 100);
</script>

<main>Camera</main>

<style>
</style>
