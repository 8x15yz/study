<template>
  <div id="app">
    <nav class="d-flex justify-content-between">
      <div>
        <h3>Hellow</h3>
      </div>
      <div class="justify-content-evenly">
        <router-link to="/">Home</router-link> |
        <router-link to="/LottoView">LottoView</router-link> |
        <router-link to="/LunchView">LunchView</router-link>
      </div>
    </nav>
    <router-view/>
  </div>
</template>

<style>
#app {
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 20px;
  background-color: pink;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
