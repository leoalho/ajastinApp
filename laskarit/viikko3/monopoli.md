```mermaid
classDiagram
	class pelilauta
	class ruutu{
		seuraava ruutu
	}
	class pelinappula
	class pelaaja
	class noppa
	pelilauta <|-- pelaaja
	pelilauta <|-- ruutu
```
	
