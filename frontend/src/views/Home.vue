<script>
import { resetTracking } from '@vue/reactivity';

  export default{
    data() {
      return {
        obj: []
      }
    },
    mounted() {
      this.getAllDatas();
    },
    methods: {
      async getAllDatas() {
        const response = await fetch('http://localhost:5000')
        .then(e => e.json())

        for(let i in response) {
          this.obj.push(response[i]);
        }
      },
      showDatas() {
        const select = document.querySelector('#select');
        const code = document.querySelector('.code');

        switch(select.value) {
          case 'Gabriel':
            code.innerHTML = JSON.stringify(this.obj[0], null, 2);
            break;
          case 'Rafael':
          code.innerHTML = JSON.stringify(this.obj[1], null, 2);
            break;
          case 'Rosenice':
          code.innerHTML = JSON.stringify(this.obj[2], null, 2);
            break;
          default:
            console.log('Erro!');
            break;
        }
      }
    }
  }
</script>

<template>
  <main>
    <h1>You are in Homepage!</h1>
    <select id="select">
      <option v-for="item in this.obj" :key="item.id" :value="item.nome">{{item.nome}}</option>
    </select>
    <div class="codeContainer">
      <div class="codeTitleContainer">
        <p>JSON Code</p>
      </div>
      <pre class="code"></pre>
    </div>
    <button @click="showDatas();">Verificar dados</button>
  </main>
</template>

<style scoped>
  #select {
    display: block;
  }
  button {
    cursor: pointer;
  }
  .codeContainer {
    background-color: #000;
    width: 400px;
    height: 300px;
    color: #fff;
    overflow: auto;
    font-size: 20px;
  }
  .codeTitleContainer {
    width: 100%;
    display: flex;
    justify-content: center;
    border-bottom: 1px solid grey;
  }
  .code {
    font-size: 14px;
  }
</style>
