FROM tomcat:latest
ENV TZ=Asia/Seoul
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN rm -Rf /usr/local/tomcat/webapps/ROOT
COPY target/spring.war /usr/local/tomcat/webapps/ROOT.war
ENV JAVA_OPTS="-Dserver.type=dev"