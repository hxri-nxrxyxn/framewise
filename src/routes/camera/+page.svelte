<script>
    import Nav from "$lib/Nav.svelte";
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
    }, 400);
</script>

<Nav message="WEBSOCKET" bold="READY" />
<main>
    <h1 class="head" id="message">LOADING</h1>
    <section>
        <label>PREVIEW</label>
        <div class="polaroid">
            <div class="polaroid__image" id="pimage"></div>
        </div>
    </section>
    <section>
        <label>SCORE</label>
        <div class="meter">
            <p class="meter__pill"></p>
            <p class="meter__pill"></p>
            <p class="meter__pill"></p>
            <p class="meter__pill"></p>
            <p class="meter__pill"></p>
            <p class="meter__pill"></p>
            <p class="meter__pill"></p>
            <p class="meter__pill"></p>
            <p class="meter__pill"></p>
            <p class="meter__pill"></p>
            <p class="meter__pill"></p>
            <p class="meter__pill"></p>
            <p class="meter__pill"></p>
            <p class="meter__pill"></p>
            <p class="meter__pill"></p>
            <p class="meter__pill"></p>
            <p class="meter__pill"></p>
            <p class="meter__pill"></p>
            <p class="meter__pill"></p>
            <p class="meter__pill"></p>
            <p class="meter__pill active"></p>
            <p class="meter__pill"></p>
        </div>
    </section>
</main>

<div class="shot">
    <div class="shot__info">
        <h1>5</h1>
        <p>TOKENS LEFT</p>
    </div>
    <div class="shot__capture">
        <div class="shot__circle">
            <div class="shot__circle--inner"></div>
        </div>
    </div>
</div>

<style>
    main {
        padding-bottom: 25vh;
    }
    section {
        margin-top: 2rem;
    }
    label {
        color: var(--color-primary);
        font-weight: 600;
        padding-bottom: 0.5rem;
        display: block;
        font-size: 0.75rem;
    }
    .polaroid {
        height: 60vh;
        border: 1px solid var(--color-border-light);
        background: white;
    }
    .polaroid__image {
        margin: 2rem;
        height: 70%;
    }
    .meter {
        display: flex;
        justify-content: space-between;
        background: white;
    }
    p.meter__pill {
        display: block;
        height: 1rem;
        width: calc((100vw - 4rem) / 320);
        background: var(--color-primary);
    }
    p.active {
        height: 2rem;
        width: calc((100vw - 4rem) / 120);
    }
    .shot {
        position: fixed;
        bottom: 0;
        width: 100%;
        background: #fff;
        border-top: 1px solid var(--color-border-light);
        min-height: 10vh;
        display: flex;
        justify-content: space-between;
    }
    .shot__info {
        padding: 2rem;
    }
    .shot__info h1 {
        font-family: "Inter";
        font-weight: 700;
        color: var(--color-primary);
    }
    .shot__info p {
        font-weight: 700;
        font-size: 0.75rem;
    }
    .shot__capture {
        display: flex;
        width: 40%;
        justify-content: center;
        align-items: center;
    }
    .shot__circle {
        background: var(--color-primary);
        width: 8vh;
        height: 8vh;
        display: flex;
        justify-content: center;
        align-items: center;
        border-radius: 50%;
        border: 1px solid var(--color-border-light);
    }
    .shot__circle--inner {
        background: white;
        width: 80%;
        height: 80%;
        border-radius: 50%;
        border: 1px solid var(--color-border-light);
        animation: breathe 2s ease-in-out infinite; /* Adjust timing as needed */
    }
    @keyframes breathe {
        0% {
            transform: scale(1);
        }
        50% {
            transform: scale(0.9); /* Slightly smaller */
        }
        100% {
            transform: scale(1);
        }
    }
</style>
