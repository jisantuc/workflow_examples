import java.io._
import org.apache.spark.SparkContext
import org.apache.spark.SparkContext._
import org.apache.spark.SparkConf

object SparkApp {

  def main(args: Array[String]) {
    val conf = new SparkConf().setAppName("wordcount.scala")
    val sc = new SparkContext(conf)
    sc.hadoopConfiguration.set(
      "fs.s3n.awsAccessKeyId",
      sys.env("AWS_ACCESS_KEY_ID")
    )
    sc.hadoopConfiguration.set(
      "fs.s3n.awsSecretAccessKey",
      sys.env("AWS_SECRET_ACCESS_KEY")
    )

    val wc = sc.textFile(args(0))
      .flatMap(line => line.split(" "))
      .map(word => word.replace(",", "").toLowerCase())
      .map(word => (word, 1))
      .reduceByKey(_ + _)
      .sortBy(pair => pair._2, false)
      .collect()

    val stringedArray = wc.mkString(" \n")
    val writer = new PrintWriter(new File(args(1)))
    writer.write(stringedArray)
    writer.close()

  }
}
