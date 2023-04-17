import { postRequest } from "./default";

type PostLoginResponse = {
    token: string;
};

export const cadastro = async (
    cpf: string,
    email:string,
    senha:string
): Promise<PostLoginResponse> => {
    const response = await postRequest('/conta/cadastro',{
        "cpf": cpf,
        "email": email,
        "senha": senha,
        "tipo": "cliente"
    }).then((value) => {
        console.log('logado');
        return value
    }).catch(reason => {
        console.log(reason);
        return reason
    });
    console.log(response)
    return response;
};
