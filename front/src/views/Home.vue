<template>
  <div>
    <!-- <transition name="menu">
      <div id="menu" v-if="showMenu">
        <ul>
          <li><router-link :to="{name: 'OMG' }">PROFILE</router-link></li>
          <li><router-link :to="{name: 'Members' }">MEMBERS</router-link></li>
          <li><router-link :to="{name: 'Albums' }">ALBUMS</router-link></li>
          <li>VIDEO</li>
        </ul>
      </div>
    </transition> -->
    <!-- <header class="d-flex justify-content-between align-items-center">
      <div><a href="/">OH MY GIRL</a></div>
      <i @click="showMenus" class="fas fa-bars"></i>
    </header> -->
    <!-- <div id="icons" class="d-flex">
      <a target="blank" href="http://ohmy-girl.com/omg_official/"><i class="fas fa-home"></i></a>
      <a target="blank" href="https://cafe.daum.net/-ohmygirl"><i class="fab fa-dochub"></i></a>
      <a target="blank" href="https://www.instagram.com/wm_ohmygirl/"><i class="fab fa-instagram"></i></a>
      <a target="blank" href="https://twitter.com/WM_OHMYGIRL"><i class="fab fa-twitter"></i></a>
      <a target="blank" href="https://www.youtube.com/channel/UC-qYkzKFdekoEniRu_FS3zg"><i class="fab fa-youtube"></i></a>
      <a target="blank" href="https://www.vlive.tv/channel/F51143"><i class="far fa-hand-peace"></i></a>
    </div> -->
    <div id="album-info">
      <p id="album-name">Dear OHMYGIRL</p>
      <a target="blank" href="https://www.youtube.com/watch?v=HzOjwL7IP_o"><i class="fab fa-youtube"></i></a><span> Dun Dun Dance</span>
    </div>
    <div id="bg"></div>
  </div>
</template>

<script>

export default {
  name: 'Home',
  components: {
    
  },
  data: function () {
    return {
    }
  },
  created: function () {
    this.$emit('sHome')
  },
}
</script>

<style scoped>
  #bg {
    position: absolute;
    background: url('../assets/Concept.jpg');
    background-size: cover;
    background-position: center;
    left: 0;
    top: 0;
    width: 100vw;
    height: 100vh;
    overflow: hidden;
    z-index: 1;
    animation-name: bg;
    animation-duration: 1s;
  }

  @keyframes bg {
    0% { opacity: 0;}
    100% { opacity: 1;}
  }

  #bg::after {
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    content: "";
    height: 100%;
    width: 100%;
    background: rgba(0,0,0, 0.5);
    z-index: 1;
  }

  /* header {
    position: fixed;
    width: 100%;
    height: 120px;
    top: 0;
    left: 0;
    color: rgb(255, 255, 255);
    z-index: 3;
    font-size: 2.5rem;
    font-weight: 1000;
    padding: 2rem 5rem 0 5rem;
    font-family: 'Stint Ultra Condensed', cursive;
    letter-spacing: 2px;
  }

  header > div > a {
    color: rgb(255, 255, 255);
    text-decoration: none;
    transition: color 1s 0.3s;
  }

  header > i {
    cursor: pointer;
    transition: color 1s 0.3s;
  } */

  /* #icons {
    z-index: 3;
    position: absolute;
    left: 5rem;
    bottom: 3rem;
    font-size: 2rem;
    transition: transform .2s;
  }

  #icons > a {
    color: rgb(255, 255, 255);
    padding-right: 2rem;
    transition: color 1s 0.3s;
  }

  #icons i {
    transition: transform .2s;
  }

  #icons i:hover{
    transform: translate(0, -30%);
  } */

  #album-info {
    z-index: 2;
    color: white;
    position: absolute;
    right: -5rem;
    top: 15%;
    text-align: end;
    font-weight: bold;
    font-family: 'Dosis', sans-serif;
    animation: album-info 1s 0.4s forwards;
    opacity: 0;
  }

  @keyframes album-info {
    0% { opacity: 0;}
    100% { opacity: 1; right: 5rem;}
  }


  #album-name {
    font-size: 5rem;
    margin: 0;
    letter-spacing: 10px;
    color: rgb(244, 166, 215);
    text-shadow: 7px 7px 5px rgb(0,0,0, 0.7);
  }

  #album-info > a > i {
    font-size: 3.5rem;
    color: white;
    transition: all 0.3s;
    letter-spacing: 10px;
    text-shadow: 7px 7px 5px rgb(0,0,0, 0.7);
  }

  #album-info > a > i:hover {
    transform: scale(0.8);
    color: red;
  }

  #album-info > span {
    font-size: 3.5rem;
    font-weight: lighter;
    color: rgb(238, 226, 159);
    text-shadow: 7px 7px 5px rgb(0,0,0, 0.7);
  }

  /* #menu {
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
    color: black;
    transform: translate(-50%);
    list-style: none;
    font-weight: bold;
    font-size: 2.5rem;
    text-align: start;
    font-family: 'Dosis', sans-serif;
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
  } */
</style>