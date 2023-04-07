<template>
  <div class="contact">
    <div class="contact-header">
      <h1>Contact Us</h1>
    </div>
    <div class="contact-content">
      <form>
        <div class="form-group">
          <label for="name">Name</label>
          <input type="text" class="form-control" id="name" placeholder="Enter your name" required>
        </div>
        <div class="form-group">
          <label for="email">Email address</label>
          <input type="email" class="form-control" id="email" placeholder="Enter your email" required>
        </div>
        <div class="form-group">
          <label for="message">Message</label>
          <textarea class="form-control" id="message" rows="5" placeholder="Enter your message" required></textarea>
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: "Contact",
};
</script>

<style scoped>
.contact {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100%;
  padding: 2rem;
}

.contact-header {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-bottom: 2rem;
}

.contact-header h1 {
  font-size: 3rem;
  margin-bottom: 0.5rem;
}

.contact-content {
  width: 100%;
  max-width: 600px;
}

.form-group {
  margin-bottom: 2rem;
}

.form-group label {
  display: block;
  font-size: 1.2rem;
  margin-bottom: 0.5rem;
}

.form-control {
  width: 100%;
  padding: 1rem;
  font-size: 1.2rem;
  border-radius: 0;
  border: 1px solid #ccc;
}

textarea.form-control {
  resize: none;
}

.btn-primary {
  background-color: #007bff;
  border: none;
  border-radius: 0;
  padding: 1rem 2rem;
  font-size: 1.2rem;
  margin-top: 2rem;
  width: 100%;
  max-width: 400px;
  transition: background-color 0.2s ease;
}

.btn-primary:hover {
  background-color: #0062cc;
}
</style>