<template>
  <div id="app">
    <transition name="menu">
      <div id="menu" v-if="showMenu">
        <ul>
          <li @click="isHomeFalse"><router-link :to="{name: 'OMG' }">HISTORY</router-link></li>
          <li @click="isHomeFalse"><router-link :to="{name: 'Members' }">MEMBERS</router-link></li>
          <li @click="isHomeFalse"><router-link :to="{name: 'Albums' }">ALBUMS</router-link></li>
          <li>VIDEO</li>
        </ul>
      </div>
    </transition>
    <header class="d-flex justify-content-between align-items-center">
      <div @click="isHomeTrue"><router-link :to="{ name: 'Home' }">OH MY GIRL</router-link></div>
      <i @click="showMenus" class="fas fa-bars"></i>
    </header>
    <div id="icons" class="d-flex">
      <a target="blank" href="http://ohmy-girl.com/omg_official/"><i class="fas fa-home"></i></a>
      <a target="blank" href="https://cafe.daum.net/-ohmygirl"><i class="fab fa-dochub"></i></a>
      <a target="blank" href="https://www.instagram.com/wm_ohmygirl/"><i class="fab fa-instagram"></i></a>
      <a target="blank" href="https://twitter.com/WM_OHMYGIRL"><i class="fab fa-twitter"></i></a>
      <a target="blank" href="https://www.youtube.com/channel/UC-qYkzKFdekoEniRu_FS3zg"><i class="fab fa-youtube"></i></a>
      <a target="blank" href="https://www.vlive.tv/channel/F51143"><i class="far fa-hand-peace"></i></a>
    </div>
    <router-view @sHome="isHomeTrue"/>
  </div>
</template>

<script>
  export default {
    name: 'Home',
    components: {
      
    },
    data: function () {
      return {
        showMenu: false,
        isHome: false,
      }
    },
    methods: {
      showMenus: function () {
        this.showMenu = !this.showMenu
        const omg = document.querySelector('header a')
        const i = document.querySelector('header i')
        const icons = document.querySelectorAll('#icons a')
        if (this.showMenu === false && this.isHome === true) {
          omg.style.color = 'white'
          i.style.color = 'white'
          icons.forEach(icon => icon.style.color = 'white')
        } else if (this.showMenu === true && this.isHome === true) {
          omg.style.color = 'black'
          i.style.color = 'black'
          icons.forEach(icon => icon.style.color = 'black')
        } else if (this.showMenu === false && this.isHome === false) {
          omg.style.color = 'black'
          i.style.color = 'black'
          icons.forEach(icon => icon.style.color = 'black')
        }
      },
      isHomeTrue: function () {
        this.isHome = true
        this.showMenu = false
        const omg = document.querySelector('header a')
        if (omg === null) {
          window.addEventListener('load', function () {
            const omg = document.querySelector('header a')
            const i = document.querySelector('header i')
            const icons = document.querySelectorAll('#icons a')
            omg.style.color = 'white'
            i.style.color = 'white'
            icons.forEach(icon => icon.style.color = 'white')
          })
        } else {
          const omg = document.querySelector('header a')
          const i = document.querySelector('header i')
          const icons = document.querySelectorAll('#icons a')
          omg.style.color = 'white'
          i.style.color = 'white'
          icons.forEach(icon => icon.style.color = 'white')
        }
      },
      isHomeFalse: function () {
        this.isHome = false
        this.showMenu = false
      },
    },
  }
</script>



<style>
  body {
    overflow: hidden;
  }

  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    background-color: black;
    width: 100vw;
    height: 100vh;
    background: white;
  }

  header {
    position: fixed;
    width: 100%;
    height: 10vh;
    top: 0;
    left: 0;
    color: black;
    z-index: 3;
    font-size: 2.5rem;
    font-weight: 1000;
    padding: 2rem 5% 0 5%;
    font-family: 'Stint Ultra Condensed', cursive;
    letter-spacing: 2px;
  }

  header > div > a {
    color: black;
    text-decoration: none;
    transition: color 1s 0.3s;
  }

  header > div > a:hover {
    text-decoration: none;
    color: white;
  }

  header > i {
    cursor: pointer;
    transition: color 1s 0.3s;
  }

  #menu {
    position: absolute;
    top: 0;
    left: 0;
    height: 100vh;
    width: 100vw;
    background-color: white;
    overflow: hidden;
    z-index: 3;
  }

  #menu > ul {
    position: absolute;
    left: 50%;
    top: 30%;
    transform: translate(-50%);
    list-style: none;
    font-weight: bold;
    font-size: 2.5rem;
    text-align: start;
    font-family: 'Dosis', sans-serif;
    margin: 0;
    padding: 0;
  }

  #menu a {
    color: black;
    text-decoration: none;
  }

  #menu li {
    transition: transform 0.5s;
  }

  #menu li:hover {
    transform: translate(10%);
  }

  .menu-enter-active {
    animation: showMenu .5s;
  }

  .menu-leave-active {
    animation: showMenu .5s reverse;
  }

  @keyframes showMenu {
    0% { height: 0%; }
    100% { height: 100vh; }
  }

  #icons {
    z-index: 3;
    position: absolute;
    left: 5%;
    bottom: 0;
    font-size: 2rem;
    height: 10vh;
    transition: transform .2s;
  }

  #icons > a {
    color: black;
    padding-right: 2rem;
    transition: color 1s 0.3s;
  }

  #icons i {
    transition: transform .2s;
  }

  #icons i:hover{
    transform: translate(0, -30%);
  }

</style>
