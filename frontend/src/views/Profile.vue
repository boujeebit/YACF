<template>

<div class="container" style="margin-top: 20px;">
    <div class="row">
        <div class="col-sm-3">
            <div class="text-center">
                <img src="http://ssl.gstatic.com/accounts/ui/avatar_2x.png" class="avatar img-circle img-thumbnail" alt="avatar">
                <input type="file">
            </div>
        </div>
        <div class="col-sm-9">

            <label for="first_name"><strong>First name</strong></label>
            <input type="text" class="form-control" v-model="this.$store.state.user.user.firstName">

            <label for="last_name"><strong>Last name</strong></label>
            <input type="text" class="form-control" v-model="this.$store.state.user.user.lastName">

            <label for="email"><strong>Email</strong></label>
            <input type="email" class="form-control">

            <label for="password"><strong>Password</strong></label>
            <input type="password" class="form-control">
            
            <label for="password2"><strong>Verify</strong></label>
            <input type="password" class="form-control">

            <hr>

            <label for="password2"><strong>Team</strong></label>
            <input type="password" class="form-control" disabled>


            <!-- <div class="form-group">
                <div class="col-xs-12">
                    <br>
                    <button class="btn btn-lg btn-success" type="submit"><i class="glyphicon glyphicon-ok-sign"></i> Save</button>
                    <button class="btn btn-lg" type="reset"><i class="glyphicon glyphicon-repeat"></i> Reset</button>
                </div>
            </div> -->
        </div>
    </div>
</div>

</template>

<script>

export default {
  name: '',
  data () {
    return {

    }
  },
  methods: {
      
  }
}
</script>

<style scoped>
label {
    margin-top: 10px;
}

.img-circle {
    border-radius: 50%;
}
</style>