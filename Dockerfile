# Build stage with Maven & JDK 21
FROM maven:3.9.6-eclipse-temurin-21 AS build
COPY . /vprofile-updated
WORKDIR /vprofile-updated
RUN mvn clean install

# Slim Tomcat runtime
FROM tomcat:10.1-jdk21-temurin
LABEL "Project"="Vprofile"
LABEL "Author"="vickey"
RUN rm -rf /usr/local/tomcat/webapps/*
COPY --from=build /vprofile-updated/target/vprofile-v2.war /usr/local/tomcat/webapps/ROOT.war

EXPOSE 8080
CMD ["catalina.sh", "run"]
