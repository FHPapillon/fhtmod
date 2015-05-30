package com.fht.base;

public class StringManager
{
      public static String Left(String text, int length)
      {
            return text.substring(0, length);
      }

      public static String Right(String text, int length)
      {
            return text.substring(text.length() - length, length);
      }  

      public static String Mid(String text, int start, int end)
      {
            return text.substring(start, end);
      }  

      public static String Mid(String text, int start)
      {
            return text.substring(start, text.length() - start);
      }
}