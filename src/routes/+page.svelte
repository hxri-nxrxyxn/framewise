<script>
  import { handleBackButton, checkUser, logout } from "../script";

  handleBackButton("/");
  const user = checkUser();
  console.log(user);
</script>

<h1>this is my home</h1>
<a href="/login">login</a>
<a href="/signup">signup</a>
<a href="/camera">camera</a>
<button onclick={logout}>logout</button>
