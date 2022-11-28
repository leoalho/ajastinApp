```mermaid
classDiagram
    main_service "1" -- "1" timer
    main_service "1" -- "1" user
    user "1" -- "*" project
    main_service -.-> project
    main_service -- project-repository
    main_service -- user_repository
```