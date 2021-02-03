## conrad_assignment_streaming

## Assignment
Take any of your ML projects which is ​done​( ​it could be MNIST from tutorials or Iris classification or any done project ​) and ​create a streaming pipeline for prediction​. ​Dockerize​ the application. Additionally please show if requests are coming from more than 2 channels how the application will handle the requests. Describe the application in the ​Readme​ file.

### SET UP NETWORK
```$ docker network create kafka-network```

### START
Spin up the local single-node Kafka cluster:

```$ docker-compose -f docker-compose.kafka.yml up -d```

Check the cluster is up and running (wait for "started" to show up):

```$ docker-compose -f docker-compose.kafka.yml logs -f broker | grep "started"```

Start the message generator and the classifier:

```$ docker-compose up -d```

### TEST THE RESULT
Check the result of the classification (in new terminal window):

```$ docker-compose -f docker-compose.kafka.yml exec broker kafka-console-consumer --bootstrap-server localhost:9092 --topic streaming.transactions.predict```

### EXAMPLE OF THE RESULT
{"sepal length": 5.7, "sepal width": 3.2, "petal length": 6.4, "petal width": 2.3, "predicted": 2}
