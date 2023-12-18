# Proxy

Provides a surrogate or a placeholder that controls access to another object.

Proxies solve problems that are access-related. 

**Remote Proxy** - a local representative to a remote object.

**Virtual Proxy** - controls access to a resource that is expensive to create.

**Protection Proxy** - access management. 


## Exemplary Diagram

```
          ┌─────────────────┐ 
          │InterfaceSubject │
          ├─────────────────┤ 
          │request()        │ 
          └─┬────────────┬──┘  
            △            △
       ┌────┘            └─────┐
┌──────┴────────┐       ┌──────┴────────┐ 
│RealSubject    │       │Proxy          │
├───────────────┤       ├───────────────┤ 
│request()      │ <───*─│request()      │ 
└───────────────┘     │ └───────────────┘  
                      │
                      └─ controlled here
```
The instantiation of the RealSubject may be expensive. 
The Proxy is responsible for instantiating the real subject.
The value may be stored in state at the proxy after the first time. 

The request() from the Proxy to the RealSubject is controlled. 
