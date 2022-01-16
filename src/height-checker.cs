public class Solution {
  public int HeightChecker(int[] heights) {
    int[] heightsSorted = new int[heights.Length];

    for (int i = 0; i < heights.Length; i++)
      heightsSorted[i] = heights[i];

    Array.Sort(heightsSorted);

    int c = 0;
    for (int i = 0; i < heights.Length; i++)
      if (heightsSorted[i] != heights[i])
        c++;

    return c;
  }
}
