import React, { FormEvent, useState } from "react";
import { login } from "../services/login"
import axios from "axios";
interface LoginFormProps  {
  email: string;
  senha: string;
}

export const TelaLogin: React.FC = () => {
  const [usuario, setUsuario] = useState<LoginFormProps>({
    email: "",
    senha: "",
  });
  const handleIrAoHome = () => {
    // Redireciona para a tela de pagamento com os dados do pedido
    window.location.href = `/`;
  };
  /*const handleSubmit = (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    if( usuario.email !== "" && usuario.senha !== "") {
        login(usuario.email, usuario.senha)
          .then(({ token, error }) => {
            if (error) {
                console.log(error);
            } else {
                console.log("la", token);
                localStorage.setItem("token", token);
            }
      })
    }
  };*/
  const handleSubmit = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    if (usuario.email !== "" && usuario.senha !== "") {
      try {
        const body = {
          "email": usuario.email,
          "senha": usuario.senha,
          "tipo": "cliente"
        };
  
        const response = await axios.post('http://localhost:3030/conta/login', body); // substitua a URL pela sua rota de login
  
        console.log(response.data); // exibe o retorno da API
        
        localStorage.setItem("token",JSON.stringify(response.data))
        window.location.href = `/produtos`;
        }catch (error) {
        console.log(error);
      }
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
          <button onClick={handleIrAoHome} type="button" style={{ width: '130px' }}>Voltar</button>
        </div>

      </form>
    </div>
  );
};