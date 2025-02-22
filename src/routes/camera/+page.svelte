<script>
  import {
    startWebsocket,
    startCamera,
    sendToBackend,
    cameraBack,
  } from "../../script";
  import { onMount } from "svelte";
  cameraBack();

  onMount(() => {
    startWebsocket();
    startCamera();
  });
</script>

<main>Camera</main>

<style>
</style>
