<script>
    import { handleBackButton, checkUser, logout } from "../script";
    handleBackButton("/");
</script>

<nav>
    <p>WEBSOCKET <b>CONNECTED</b></p>
    <img src="/lock.svg" alt="hey" />
</nav>
<main>
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
    <div class="buttons">
        <div class="button">TRY</div>
        <div class="button">
            LOGIN
            <span>FX</span>
        </div>
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
    .button:first-child {
        background: var(--color-primary);
        color: white;
    }
    .button:last-child {
        margin-left: 10%;
    }
    .button span {
        position: absolute;
        right: -0.75rem;
        top: -0.5rem;
        transform: rotate(3deg);
        background: var(--color-secondary);
        padding: 0.15rem 1rem;
        font-weight: 600;
        font-size: 0.75rem;
        border: 1px solid var(--color-border);
    }
    p.tagline {
        text-align: center;
        margin: 2rem 0;
        font-family: Baskervville;
        font-style: italic;
        font-weight: 100;
    }
</style>
