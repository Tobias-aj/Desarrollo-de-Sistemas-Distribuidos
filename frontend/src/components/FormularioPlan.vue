<template>
  <div class="form-container">
    <h2>Alta de un Nuevo Plan de Recolección</h2>
    <form @submit.prevent="crearPlan">
      <div class="form-group">
        <label for="nombre_plan">Nombre del Plan</label>
        <input type="text" id="nombre_plan" v-model="nombre_plan" required />
      </div>
      
      <!-- <div class="form-group">
        <label for="fecha_inicio">Fecha de Inicio</label>
        <input type="date" id="fecha_inicio" v-model="fecha_inicio" required />
      </div>
      
      <div class="form-group">
        <label for="fecha_fin">Fecha de Fin</label>
        <input type="date" id="fecha_fin" v-model="fecha_fin" required />
      </div> -->
      
      <div class="form-group">
        <label for="tipo_material">Tipo de Material</label>
        <select id="tipo_material" v-model="tipo_material" required>
          <option value="vidrio">Vidrio</option>
          <option value="plastico">Plástico</option>
          <option value="carton">Cartón</option>
          <option value="metal">Metal</option>
          <option value="cable">Cable</option>
          <option value="envases">Envases</option>
        </select>
      </div>

      <div class="form-group">
        <label for="cantidad">Cantidad</label>
        <input type="number" id="cantidad" v-model="cantidad" required />
      </div>
      
      <div class="form-group">
        <label for="area_recoleccion">Área de Recolección</label>
        <select id="area_recoleccion" v-model="area_recoleccion" required>
          <option value="comercios">Comercios</option>
          <option value="hogares">Hogares</option>
          <option value="fábricas">Fábricas</option>
          <option value="talleres">Talleres</option>
        </select>
      </div>
      
      <button type="submit" class="btn-submit">Crear Plan</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      nombre_plan: '',
      // fecha_inicio: '',
      // fecha_fin: '',
      tipo_material: '',
      cantidad: '',
      area_recoleccion: '',
    }
  },
  methods: {
    crearPlan() {
      const plan = {
        nombre_plan: this.nombre_plan,
        // fecha_inicio: this.fecha_inicio,
        // fecha_fin: this.fecha_fin,
        tipo_material: this.tipo_material,
        cantidad: this.cantidad,
        area_recoleccion: this.area_recoleccion,
        frecuencia: this.frecuencia
      };

      // Enviar los datos al backend Flask
      fetch('http://127.0.0.1:5000/api/crear-plan', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(plan)
      })
      .then(response => response.json())
      .then(data => {
        alert(data.message);
      })
      .catch(error => {
        console.error('Error:', error);
      });
    }
  }
}
</script>

<style scoped src="../css/FormularioPlan.css"></style>