# docker_compose

Quelles sont les étapes pour construire une image Docker à partir d’un fichier Dockerfile ?
Créez un Dockerfile, ajoutez les instructions nécessaires, puis exécutez docker build.

Quel est le rôle de la commande docker build ? Donnez un exemple de syntaxe.
Elle crée une image Docker à partir d'un Dockerfile, par exemple : docker build -t nom_image:version ..

Quelle est la différence entre les instructions FROM, WORKDIR et CMD dans un fichier Dockerfile ?
FROM définit l’image de base, WORKDIR le répertoire de travail, et CMD la commande par défaut.

Pourquoi est-il important de spécifier une image de base dans le fichier Dockerfile ?
Elle fournit un environnement préconfiguré pour démarrer le projet.

Une fois l’image construite, comment pouvez-vous exécuter un conteneur basé sur cette image ?
Utilisez docker run -d -p 8080:8080 nom_image:version.

Si vous modifiez le fichier source Python utilisé dans le conteneur, que devez-vous faire pour refléter ces modifications dans votre conteneur ?
Reconstruisez l’image avec docker build et relancez le conteneur.