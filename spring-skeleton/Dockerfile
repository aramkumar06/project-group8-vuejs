FROM tomcat:8.0.51-jre7-alpine  # docker 안의 tomcat8 셋팅, 사내 백오피스는 자바 7 사용.

ENV TZ=Asia/Seoul ## 타임존 서울로 설정 후 적용
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN rm -Rf /usr/local/tomcat/webapps/ROOT # 기존 도커안의 tomcat의 루트 경로 삭제 
COPY target/spring.war /usr/local/tomcat/webapps/ROOT.war # 루트 경로에 복사
ENV JAVA_OPTS="-Dserver.type=dev" # 서버타입 설정, 프로퍼티 파일로 개발 운영 환경 구분..