<script>
    import { onMount } from "svelte";
    import { handleBackButton, checkUser, logout } from "../script";
    import { fade, fly } from "svelte/transition";
    import Nav from "$lib/Nav.svelte";
    handleBackButton("/");

    let animatedElement;

    onMount(() => {
        if (animatedElement) {
            animatedElement.classList.add("animate--fx");
        }
    });
</script>

<Nav message="READY TO" bold="LAUNCH" />
<section>
    <!-- svelte-ignore a11y_distracting_elements -->
    <marquee scrollamount="12" behavior="scroll">
        <h1 class="marquee">PROFESSIONAL SHOTS</h1>
    </marquee>
    <!-- svelte-ignore a11y_distracting_elements -->
    <h1>FRAMEWISE</h1>
    <!-- svelte-ignore a11y_distracting_elements -->
    <marquee scrollamount="10" behavior="scroll">
        <h1 class="marquee">SHOTS THAT MAKE THE MEMORIES</h1>
    </marquee>
</section>

<main>
    <div class="buttons">
        <a href="/camera">
            <div class="button button--orange">TRY</div>
        </a>
        <a href="/login">
            <div class="button">
                LOGIN
                <span bind:this={animatedElement}>FX</span>
            </div>
        </a>
    </div>
    <p class="tagline">Made with love in India <span>❤️</span></p>
    <img src="/photoshoot.svg" alt="" class="cover" />
</main>

<style>
    section {
        padding: 3rem 0;
    }
    section h1 {
        font-style: italic;
        text-align: center;
        font-size: 3.5rem;
        line-height: 1;
    }
    section h1.marquee {
        color: var(--color-grey);
    }
    .button span {
        position: absolute;
        right: -0.75rem;
        top: -0.5rem;
        background: var(--color-secondary);
        padding: 0.15rem 1rem;
        font-weight: 600;
        font-size: 0.75rem;
        border: 1px solid var(--color-border);
        color: var(--color-grey);
    }
    .button--orange {
    }
    p.tagline {
        text-align: center;
        margin: 2rem 0;
        font-family: Baskervville;
        font-style: italic;
        font-weight: 100;
    }
    p.tagline span {
        font-style: initial;
    }
</style>
