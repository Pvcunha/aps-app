import React, { FormEvent, useState } from "react";
import { cadastro } from "../services/cadastro"

interface CadastroFormProps  {
  email: string;
  senha: string;
  cpf: string;
}

export const TelaCadastro: React.FC = () => {
  const [usuario, setUsuario] = useState<CadastroFormProps>({
    email: "",
    senha: "",
    cpf: "",
  });

  const handleSubmit = (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    cadastro(usuario.cpf, usuario.email, usuario.senha);
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

      <label htmlFor="cpf">CPF:</label>
      <input
        required
        type="text"
        name="cpf"
        value={usuario.cpf}
        onChange={handleInputChange}
      />

      <button type="submit">Cadastrar</button>
    </form>
  );
};