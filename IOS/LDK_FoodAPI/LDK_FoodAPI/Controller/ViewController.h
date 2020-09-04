//
//  ViewController.h
//  LDK_FoodAPI
//
//  Created by LE DANG KHOA on 1/19/19.
//  Copyright © 2019 LDK. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface ViewController : UIViewController<UICollectionViewDelegate, UICollectionViewDataSource, UICollectionViewDelegateFlowLayout>
{
    NSArray *recipeList;
}

@property (weak, nonatomic) IBOutlet UICollectionView *collectionRecipes;

@end

