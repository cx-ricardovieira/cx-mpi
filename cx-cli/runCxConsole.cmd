@echo off

pushd "%~dp0"
set JAVA_HOME=
set PATH=%JAVA_HOME%/bin;%PATH%

java -Xmx1024m -jar CxConsolePlugin-CLI-1.1.8.jar %*
set exitCode=%errorlevel%

popd
Exit /B %exitCode%