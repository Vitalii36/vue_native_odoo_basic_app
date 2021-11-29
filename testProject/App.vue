<template>
  <view class="container">
    <text class="text-color-primary">LOGIN</text>
    <text-input
        :style="{height: 40, width: 100, borderColor: 'gray', borderWidth: 1}"
        v-model="login"
      />
    <text class="text-color-primary">PASSWORD</text>
    <text-input
        :style="{height: 40, width: 100, borderColor: 'gray', borderWidth: 1}"
        v-model="password"
      />
    <!-- <text class="text-color-primary">{{ message }}</text> -->
    <button title="Sing In" @press="mounted" />
  </view>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      login: '',
      password: '',
      message: ''
    };
  },
  methods: {
    mounted() {
      axios.post("http://192.168.0.101:11000/" ,{ params: { login: this.login, password: this.password }}
      ).then(result => 
        {
          this.message = result.data.results;
          if (!this.message) {
            alert('Your password or login is incorrect')
          }
        }, error => {
        console.error(error);
      });
    }
  },
};
</script>

<style>
.container {
  flex: 1;
  background-color: white;
  align-items: center;
  justify-content: center;
}
.text-color-primary {
  color: blue;
  font-size: 30;
}
</style>
