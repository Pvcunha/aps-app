import cors from "cors";
import express, { NextFunction, Request, Response } from "express";
import { createProxyMiddleware } from "http-proxy-middleware";
import morgan from "morgan";

import { getServicoConsul } from "./comunicacao/host";
import servicos from "./comunicacao/servicos"

class App {
  private server;

  constructor() {
    this.server = express();
    this.server.set("trust proxy", true);
    
    this.server.use(
      cors({
        credentials: true,
        origin: "*"
      })
    );
    this.routes()
    this.server.use(morgan("dev"));
    
    this.setupProxiesMiddlewares();
  }
  private routes() {
    this.server.get('/me', (req: Request, res:Response) => {
      res.send('Ola mundo')
    })
  }
  private setupProxiesMiddlewares() {
    servicos.forEach( servico => {
      this.server.use(
        servico.path,
        createProxyMiddleware({
          target: servico.name,
          pathRewrite: (path: string) => path.replace(servico.path, ""),
          router: getServicoConsul(servico.name)
        })
      );
    });

    this.server.use((req: Request, res: Response, next: NextFunction) => {
      res.status(404).json(({message: "Rota nao encontrada"}));
    });

    this.server.use((err: Error, req: Request, res: Response, next: NextFunction) => {
      console.log(err);
      res.status(500).json({message: err.message});
    });
  }

  public getServer() {
    return this.server;
  }
};

export default App;
