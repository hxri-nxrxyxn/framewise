<script>
    export let message;
    export let bold;

    // we can fetch error statuses and custom response with messages
    // animatedNav also adds a unique touch
    import { onMount } from "svelte";
    let animatedNav;
    onMount(() => {
        if (animatedNav) {
            animatedNav.classList.add("animate--moveDown");
        }
    });
</script>

<nav bind:this={animatedNav}>
    <p>{message} <b>{bold}</b></p>
    <img src="/lock.svg" alt="hey" />
</nav>

<style>
    nav {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 0.5rem;
        padding: 1rem;
        padding-top: 2rem;
    }

    nav img {
        height: 0.75rem;
        filter: invert(16%) sepia(0%) saturate(1%) hue-rotate(315deg)
            brightness(99%) contrast(87%);
    }

    nav p {
        font-size: 0.75rem;
    }
</style>
