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
    <form onSubmit={handleSubmit}>
      <label htmlFor="email">email:</label>
      <input
        required
        type="text"
        name="email"
        value={usuario.email}
        onChange={handleInputChange}
      />

      <label htmlFor="senha">Senha:</label>
      <input
        required
        type="password"
        name="senha"
        value={usuario.senha}
        onChange={handleInputChange}
      />

      <button type="submit">Login</button>
    </form>
  );
};