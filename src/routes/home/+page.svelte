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
<div class="all">
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
        <p class="tagline">Made with love in India <span>❤️</span></p>
    </main>

    <article>
        <div class="box">
            <h1>WOMEN</h1>
            <img src="/model_pose1.jpg" alt="girl" style="width:80%" />
            <div class="buttons">
                <a href="/camera">
                    <div class="button">CLICK</div>
                </a>
            </div>
        </div>
    </article>

    <marquee>
        <div class="statement">
            <p>Style is a Statement</p>
            <p>Style is a Statement</p>
            <p>Style is a Statement</p>
            <p>Style is a Statement</p>
            <p>Style is a Statement</p>
            <p>Style is a Statement</p>
            <p>Style is a Statement</p>
            <p>Style is a Statement</p>
            <p>Style is a Statement</p>
            <p>Style is a Statement</p>
            <p>Style is a Statement</p>
            <p>Style is a Statement</p>
            <p>Style is a Statement</p>
            <p>Style is a Statement</p>
            <p>Style is a Statement</p>
            <p>Style is a Statement</p>
            <p>Style is a Statement</p>
            <p>Style is a Statement</p>
            <p>Style is a Statement</p>
            <p>Style is a Statement</p>
            <p>Style is a Statement</p>
            <p>Style is a Statement</p>
            <p>Style is a Statement</p>
            <p>Style is a Statement</p>
            <p>Style is a Statement</p>
            <p>Style is a Statement</p>
            <p>Style is a Statement</p>
            <p>Style is a Statement</p>
            <p>Style is a Statement</p>
            <p>Style is a Statement</p>
            <p>Style is a Statement</p>
            <p>Style is a Statement</p>
            <p>Style is a Statement</p>
            <p>Style is a Statement</p>
        </div>
    </marquee>

    <article>
        <div class="box">
            <h1>MEN</h1>
            <img src="/model_pose3-cr.jpg" alt="boy" style="width:80%" />
            <div class="buttons">
                <a href="/camera">
                    <div class="button">CLICK</div>
                </a>
            </div>
        </div>
    </article>
</div>

<style>
    .all {
        height: 100vh;
    }
    .all > * {
        scroll-snap-align: start;
    }
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
        margin: 2rem auto;
        font-family: Baskervville;
        font-style: italic;
        font-weight: 100;
    }
    p.tagline span {
        font-style: initial;
    }
    article {
        height: 100vh;
    }
    .box {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    .box h1 {
        font-size: 2.5rem;
        text-align: center;
        color: var(--color-elite);
        margin: 2rem 0;
    }
    .box img {
        width: 100%;
        margin-bottom: 2rem;
    }
    .box .button {
        width: 30vw;
    }
    .statement {
        display: flex;
        gap: 2.5rem;
        font-family: "Baskervville";
        font-style: italic;
        margin-bottom: 5rem;
    }
</style>
