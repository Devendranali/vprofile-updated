FROM openjdk:21-jdk-slim AS build
RUN apt-get update && apt-get install -y maven
COPY . /vprofile-updated
RUN cd /vprofile-updated && mvn clean install

FROM tomcat:10-jdk21
LABEL "Project"="Vprofile"
LABEL "Author"="vickey"
RUN rm -rf /usr/local/tomcat/webapps/*
COPY --from=build vprofile-updated/target/vprofile-v2.war /usr/local/tomcat/webapps/ROOT.war

EXPOSE 8080
CMD ["catalina.sh", "run"]

