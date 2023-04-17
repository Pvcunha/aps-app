import React, { FormEvent, useState } from "react";
import { cadastro } from "../services/cadastro"
//import { useHistory } from 'react-router-dom'

interface CadastroFormProps  {
  email: string;
  senha: string;
  cpf: string;
}

export const TelaCadastro: React.FC = () => {
  //const history = useHistory();
  const [usuario, setUsuario] = useState<CadastroFormProps>({
    email: "",
    senha: "",
    cpf: "",
  });

  const handleSubmit = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    if(usuario.email !== "" && usuario.senha !== "" && usuario.cpf!=""){
      cadastro(usuario.cpf,usuario.email,usuario.senha)
          .then(({token}) => {
              localStorage.setItem("token", token);
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
    <form onSubmit={handleSubmit} style={{ backgroundColor: "beige", height: "100vh", width: "100vw", display: "flex", flexDirection: "column", alignItems: "center" }}>
      <h1 style={{ textAlign: "center", marginBottom: "20px" }}>Cadastro</h1>

      <div style={{ display: "flex", flexDirection: "column", alignItems: "center", marginBottom: "20px" }}>
        <label htmlFor="email" style={{ marginBottom: "5px" }}>Email:</label>
        <input
          required
          type="text"
          name="email"
          value={usuario.email}
          onChange={handleInputChange}
          style={{ padding: "5px", width: "100%" }}
        />
      </div>

      <div style={{ display: "flex", flexDirection: "column", alignItems: "center", marginBottom: "20px" }}>
        <label htmlFor="senha" style={{ marginBottom: "5px" }}>Senha:</label>
        <input
          required
          type="password"
          name="senha"
          value={usuario.senha}
          onChange={handleInputChange}
          style={{ padding: "5px", width: "100%" }}
        />
      </div>

      <div style={{ display: "flex", flexDirection: "column", alignItems: "center", marginBottom: "20px" }}>
        <label htmlFor="cpf" style={{ marginBottom: "5px" }}>CPF:</label>
        <input
          required
          type="text"
          name="cpf"
          value={usuario.cpf}
          onChange={handleInputChange}
          style={{ padding: "5px", width: "100%" }}
        />
      </div>

      <div style={{ display: "flex", justifyContent: "space-between", width: "20%", marginBottom: "20px" }}>
        <button type="submit" style={{ padding: "5px", width: "40%" }}>Cadastrar</button>
        <button style={{ padding: "5px", width: "40%" }}>Voltar</button>
      </div>
    </form>

  );
};