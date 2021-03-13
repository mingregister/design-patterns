
public interface StatViewer {
    void output(Map<String, RequestStat> requestStats, long startTimeInMillis, long endTimeInMills);
  }
  
  public class ConsoleViewer implements StatViewer {
    public void output(
            Map<String, RequestStat> requestStats, long startTimeInMillis, long endTimeInMills) {
      System.out.println("Time Span: [" + startTimeInMillis + ", " + endTimeInMills + "]");
      Gson gson = new Gson();
      System.out.println(gson.toJson(requestStats));
    }
  }
  
  public class EmailViewer implements StatViewer {
    private EmailSender emailSender;
    private List<String> toAddresses = new ArrayList<>();
  
    public EmailViewer() {
      this.emailSender = new EmailSender(/*省略参数*/);
    }
  
    public EmailViewer(EmailSender emailSender) {
      this.emailSender = emailSender;
    }
  
    public void addToAddress(String address) {
      toAddresses.add(address);
    }
  
    public void output(
            Map<String, RequestStat> requestStats, long startTimeInMillis, long endTimeInMills) {
      // format the requestStats to HTML style.
      // send it to email toAddresses.
    }
  }