import React, { FormEvent, useState } from "react";
import { login } from "../services/login"

interface LoginFormProps  {
  email: string;
  senha: string;
}

export const TelaLogin: React.FC = () => {
  const [usuario, setUsuario] = useState<LoginFormProps>({
    email: "",
    senha: "",
  });

  const handleSubmit = (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    if( usuario.email !== "" && usuario.senha !== "") {
        login(usuario.email, usuario.email)
            .then(({token}) => {
                localStorage.setItem("token", "logged");
            })
            .catch(error => {
                console.log(error.response.data.message)
            })
    }
  };

  const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const {name, value } = event.target;
    setUsuario((prevUsuario) => ({
      ...prevUsuario,
      [name]: value,
    }));
  };

  return (
    <div style={{ backgroundColor: '#F5F5DC', height: '100vh' }}>
      <h1 style={{ textAlign: 'center', paddingTop: '5%' }}>Login</h1>
      <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
        <label htmlFor="email" style={{ paddingBottom: '10px' }}>Email:</label>
        <input
          required
          type="text"
          name="email"
          value={usuario.email}
          onChange={handleInputChange}
          style={{ marginBottom: '20px', width: '300px' }}
        />

        <label htmlFor="senha" style={{ paddingBottom: '10px' }}>Senha:</label>
        <input
          required
          type="password"
          name="senha"
          value={usuario.senha}
          onChange={handleInputChange}
          style={{ marginBottom: '20px', width: '300px' }}
        />

        <div style={{ display: 'flex', justifyContent: 'space-between', width: '300px' }}>
          <button type="submit" style={{ width: '130px' }}>Login</button>
          <button type="button" style={{ width: '130px' }}>Voltar</button>
        </div>

      </form>
    </div>
  );
};