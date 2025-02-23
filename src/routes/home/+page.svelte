<script>
    import { handleBackButton, checkUser, logout } from "../../script";
    import { onMount } from "svelte";
    import Nav from "$lib/Nav.svelte";
    handleBackButton("/");

    let name;

    onMount(async () => {
        const data = await checkUser();
        name = data.name;
    });
</script>

<Nav message="Hello" bold={name} />
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
            <div class="button">CONTINUE</div>
        </a>
    </div>
    <p class="tagline">made with love in India</p>
    <img src="/photoshoot.svg" alt="" class="cover" />
</main>

<style>
    section {
        padding: 5rem 0;
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
    .buttons {
        justify-content: center;
    }
    .button:first-child {
        background: var(--color-primary);
        color: white;
        width: 100%;
    }
    p.tagline {
        text-align: center;
        margin: 2rem 0;
        font-family: Baskervville;
        font-style: italic;
        font-weight: 100;
    }
    img.cover {
        width: 100vw;
    }
</style>
