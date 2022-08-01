<template>
  <div class="app flex-row align-items-center">
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-md-6">
          <div class="card mx-2">
            <div class="card-block p-2">
              <h2>Predict Breast Cancer</h2>
              <p class="text-muted">Predict the breast cancer if it's benign or malignant.</p>

              <div class="input-group mb-1">
                <span class="input-group-addon">Clump Thickness</span>
                <input type="text" class="form-control" v-model="clump_thickness" placeholder="">
              </div>

              <div class="input-group mb-1">
                <span class="input-group-addon">Unif Cell Size</span>
                <input type="text" class="form-control" v-model="unif_cell_size" placeholder="">
              </div>

              <div class="input-group mb-1">
                <span class="input-group-addon">Unif Cell Shape</span>
                <input type="text" class="form-control" v-model="unif_cell_shape" placeholder="">
              </div>

              <div class="input-group mb-1">
                <span class="input-group-addon">Marg Adhesion</span>
                <input type="text" class="form-control" v-model="marg_adhesion" placeholder="">
              </div>

              <div class="input-group mb-1">
                <span class="input-group-addon">Single Epith Cell Size</span>
                <input type="text" class="form-control" v-model="single_epith_cell_size" placeholder="">
              </div>

              <div class="input-group mb-1">
                <span class="input-group-addon">Bare Nuclei</span>
                <input type="text" class="form-control" v-model="bare_nuclei" placeholder="">
              </div>

              <div class="input-group mb-1">
                <span class="input-group-addon">Bland Chrom</span>
                <input type="text" class="form-control" v-model="bland_chrom" placeholder="">
              </div>

              <div class="input-group mb-1">
                <span class="input-group-addon">Norm Nucleoli</span>
                <input type="text" class="form-control" v-model="norm_nucleoli" placeholder="">
              </div>

              <div class="input-group mb-1">
                <span class="input-group-addon">Mistoses</span>
                <input type="text" class="form-control" v-model="mistoses" placeholder="">
              </div>

              <button type="button" class="btn btn-block btn-success" @click="predict()">Predict</button>
            </div>
            <div class="card-footer p-2">
              <div class="row">
                <div class="col-12">
                  
                  <div v-if="message" :class="{'card' : true, 'card-inverse' : true, 'card-danger' : error, 'card-success' : !error, 'text-center' : true}">
                    <div class="card-block">
                      <blockquote class="card-blockquote" >
                        <p v-html="message"></p>
                      </blockquote>
                    </div>
                  </div>
                  
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Form',
  data() {
    return {
      clump_thickness : null,
      unif_cell_size : null,
      unif_cell_shape : null,
      marg_adhesion : null,
      single_epith_cell_size : null,
      bare_nuclei : null,
      bland_chrom : null,
      norm_nucleoli : null,
      mistoses : null,
      error : false,
      message : null
    }
  },
  methods : {
    predict() {
      this.message = null
      this.error = false
      if (!this.clump_thickness ||
        !this.unif_cell_size ||
        !this.unif_cell_shape ||
        !this.marg_adhesion ||
        !this.single_epith_cell_size ||
        !this.bare_nuclei ||
        !this.bland_chrom ||
        !this.norm_nucleoli ||
        !this.mistoses ) {
          this.error = true
          this.message = "All inputs should be filled !"
          return;
        }
      axios.get('/breast/predict/?' +
      'clump_thickness=' + this.clump_thickness +
      '&unif_cell_size=' + this.unif_cell_size +
      '&unif_cell_shape=' + this.unif_cell_shape +
      '&marg_adhesion=' + this.marg_adhesion +
      '&single_epith_cell_size=' + this.single_epith_cell_size +
      '&bare_nuclei=' + this.bare_nuclei +
      '&bland_chrom=' + this.bland_chrom +
      '&norm_nucleoli=' + this.norm_nucleoli +
      '&mistoses=' + this.mistoses
      ).then(resp => {
        if (resp.data.prediction == 4) {
          this.error = true
          this.message = "<h3>Unfortunately, It's Malignant !</h3><h4>The Accuracy Rate is: %" + parseFloat(resp.data.accuracy * 100).toFixed(4) +"</h4>"
        } else if (resp.data.prediction == 2) {
          this.error = false
          this.message = "<h3>Fortunately, It's Benign !</h3><h4>The Accuracy Rate is: %" + parseFloat(resp.data.accuracy * 100).toFixed(4) +"</h4>"
        }
      })
    }
  }
}
</script>
